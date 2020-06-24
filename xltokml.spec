# -*- mode: python ; coding: utf-8 -*-

import os


block_cipher = None

package_folder = "kmldata"

pathex = os.path.join(".", package_folder)

icons_folder = os.path.join(package_folder, "ui", "icons")
icons = [
  (file.path, icons_folder)
  for file in os.scandir(icons_folder)
]
icons_json = os.path.join(package_folder, "icons.json")

a = Analysis(['xltokml.py'],
             pathex=[pathex],
             binaries=[],
             datas=[(icons_json, package_folder)]+icons,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='xltokml',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='xltokml')
