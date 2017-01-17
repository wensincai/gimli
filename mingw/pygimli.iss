; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{DC87B40B-FBCB-4FC6-BE79-9945D9D6BCF9}
AppName=pyGIMLi
AppVersion=1.0
;AppVerName=pyGIMLi 1.0
AppPublisher=pyGIMLi.org
AppPublisherURL=http://www.pygimli.org
AppSupportURL=http://www.pygimli.org
AppUpdatesURL=http://www.pygimli.org
DefaultDirName=c:\Software\pygimli
DefaultGroupName=pyGIMLi
LicenseFile=..\COPYING.rst
OutputBaseFilename=setup-pygimli
SetupIconFile=..\doc\_static\favicon.ico
Compression=lzma
SolidCompression=yes
PrivilegesRequired=none

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "C:\msys64\home\Guenther.T\py35\gimli\gimli\python\pygimli\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "c:\msys64\mingw64\bin\libopenblas.dll"; DestDir: "{app}\core"; Flags: ignoreversion
Source: "c:\msys64\mingw64\bin\libstdc++-6.dll"; DestDir: "{app}\core"; Flags: ignoreversion
Source: "c:\msys64\mingw64\bin\libwinpthread-1.dll"; DestDir: "{app}\core"; Flags: ignoreversion
Source: "c:\msys64\mingw64\bin\libquadmath-0.dll"; DestDir: "{app}\core"; Flags: ignoreversion
Source: "c:\msys64\mingw64\bin\libgcc_s_seh-1.dll"; DestDir: "{app}\core"; Flags: ignoreversion
Source: "c:\msys64\mingw64\bin\libgfortran-3.dll"; DestDir: "{app}\core"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
; Name: "{group}\pyGIMLi"; Filename: "{app}\MyProg.exe"

[Run]
;Filename: "{app}\MyProg.exe"; Description: "{cm:LaunchProgram,pyGIMLi}"; Flags: nowait postinstall skipifsilent

