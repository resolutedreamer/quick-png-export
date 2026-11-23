#!/usr/bin/env python3
import os
import re
import sys
import gi

gi.require_version('Gimp', '3.0')
from gi.repository import Gimp, GLib, Gio

class QuickPngExport(Gimp.PlugIn):
    def do_query_procedures(self):
        return ["plug-in-quick-png-export"]

    def do_set_i18n(self, name):
        return False

    def do_create_procedure(self, name):
        procedure = Gimp.ImageProcedure.new(
            self, name,
            Gimp.PDBProcType.PLUGIN,
            self.run, None
        )
        procedure.set_image_types("*")
        procedure.set_sensitivity_mask(Gimp.ProcedureSensitivityMask.ALWAYS)
        procedure.set_menu_label("Quick Export PNG (Layer Name)")
        procedure.add_menu_path("<Image>/File/")
        procedure.set_documentation(
            "Exports visible layers as a PNG named after the active layer without dialogs.",
            "Non-interactive layer-named PNG export for GIMP 3",
            name
        )
        procedure.set_attribution("Custom", "Custom", "2026")
        return procedure

    def run(self, procedure, run_mode, image, drawables, config, run_data):
        # 1. Get the first selected layer from the returned list
        selected_layers = image.get_selected_layers()
        if selected_layers and len(selected_layers) > 0:
            raw_name = selected_layers[0].get_name()
        elif drawables and len(drawables) > 0:
            raw_name = drawables[0].get_name()
        else:
            raw_name = "untitled"

        # Sanitize characters that are invalid in filenames
        clean_name = re.sub(r'[<>:"/\\|?*]', '_', raw_name).strip()
        if not clean_name:
            clean_name = "untitled"
        if not clean_name.lower().endswith(".png"):
            clean_name += ".png"

        # 2. Determine output folder (current file's directory, or Desktop fallback)
        source_file = image.get_file() or image.get_imported_file() or image.get_exported_file()
        if source_file and source_file.get_path():
            out_dir = os.path.dirname(source_file.get_path())
        else:
            out_dir = os.path.join(os.path.expanduser("~"), "Desktop")

        out_path = os.path.join(out_dir, clean_name)

        # 3. Duplicate and merge visible layers so the full composite exports
        export_img = image.duplicate()
        export_img.merge_visible_layers(Gimp.MergeType.CLIP_TO_IMAGE)

        # 4. Export non-interactively (no dialogs)
        out_gfile = Gio.File.new_for_path(out_path)
        Gimp.file_save(Gimp.RunMode.NONINTERACTIVE, export_img, out_gfile, None)

        # 5. Clean up and notify
        export_img.delete()
        image.set_exported_file(out_gfile)
        image.clean_all()
        Gimp.message(f"Exported PNG to: {out_path}")

        return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())

Gimp.main(QuickPngExport.__gtype__, sys.argv)
