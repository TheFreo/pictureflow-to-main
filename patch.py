from pathlib import Path

PATCHES = [
    {
        "file": "../apps/root_menu.c",
        "needle": """    pop_current_activity();\n    return GO_TO_ROOT;\n}""",
        "insert": """static int launch_pictureflow(void *param)\n{\n    (void)param;\n    open_plugin_add_path(ID2P(LANG_OPEN_PLUGIN),\n                 VIEWER_DIR "/pictureflow.rock",\n                 NULL);\n\n    return GO_TO_PLUGIN;\n}""",
    },
    {
        "file": "../apps/root_menu.c",
        "needle": "[GO_TO_FILEBROWSER] =   { browser, (void*)GO_TO_FILEBROWSER, &file_menu},",
        "insert": "    [GO_TO_PICTUREFLOW] = { launch_pictureflow, NULL, NULL },",
    },
        {
        "file": "../apps/root_menu.c",
        "needle": "#include \"disk.h\"",
        "insert": "#define VIEWER_DIR \"/.rockbox/rocks/demos\"",
    },
    {
        "file": "../apps/root_menu.c",
        "needle": "                        NULL, Icon_file_view_menu);",
        "insert": "\nMENUITEM_RETURNVALUE(pictureflowd, ID2P(LANG_COVER), GO_TO_PICTUREFLOW,\n             NULL, Icon_Plugin);",
    },
    {
        "file": "../apps/root_menu.c",
        "needle": """{ "files", &file_browser },""",
        "insert": """    { "pictureflow", &pictureflowd },""",
    },
    {
        "file": "../apps/root_menu.h",
        "needle": "GO_TO_SYSTEM_SCREEN,",
        "insert": "    GO_TO_PICTUREFLOW,",
    },
{
        "file": "../apps/lang/english.lang",
        "needle": """    general_purpose_led: "Use LED indicators"\n  </voice>\n</phrase>""",
        "insert": """<phrase>\n  id: LANG_COVER\n  desc: go to pictureflow\n  user: core\n  <source>\n    *: "PictureFlow"\n  </source>\n  <dest>\n    *: "PictureFlow"\n  </dest>\n  <voice>\n    *: "PictureFlow"\n  </voice>\n</phrase>""",
    }
]

for p in PATCHES:
    path = Path(p["file"])
    text = path.read_text()

    if not path.exists():
        print(f"{path}: file not found")
        continue

    if p["insert"].strip() in text:
        print(f"{path}: already patched")
        continue

    if p["needle"] not in text:
        raise RuntimeError(f"{path}: the desired string was not found")

    text = text.replace(p["needle"], p["needle"] + "\n" + p["insert"])
    path.write_text(text)

    print(f"{path}: OK")
