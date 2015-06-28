from distutils.core import setup
import py2app, sys, os, shutil
import subprocess

sys.argv.append('py2app')

if os.path.exists('build'):
	shutil.rmtree('build')

if os.path.exists('dist'):
	shutil.rmtree('dist')


setup(
	name="Basement Builder",
	version="0.1",
	author="Zatherz, Tempus, Jean-Alphonse",
	author_email="Zatherz@linux.pl, Tempus@chronometry.ca",
	app=["BasementBuilder.py"],
	options={"py2app": {
		"argv_emulation": True, 
		"includes": ["sip", "qtLibPathFacade"],
		"iconfile": "resources/UI/BasementBuilder.icns",
		"resources": "resources"
		}},
	setup_requires=["py2app"] 
)

# print("copy plugins")
# subprocess.call(["cp", "-r", "PlugIns", "dist/Basement Builder.app/Contents/PlugIns"])
# subprocess.call(["cp", "qt.conf", "dist/Basement Builder.app/Contents/Resources/qt.conf"])



# This shitty mac deploy simply won't work. here are some things:
#
#	- you'll need libqcocoa.dylib from your qt plugins/platforms directory, and you should put it into .app/Contents/PlugIns
#	- you should touch .app/Contents/Resources/qt.conf
#


# Some non-working snippets

# sys.argv.append('-platformpluginpath')
# sys.argv.append('/Users/Zatherz/Desktop/Basement Builder/Basement-Builder/dist/Basement Renovator.app/Contents/Resources/PlugIns')

# QCoreApplication.addLibraryPath('/Users/Zatherz/Desktop/Basement Builder/Basement-Builder/dist/Basement Renovator.app/Contents/')

# os.system('export QT_PLUGIN_PATH="{0}/PlugIns"'.format(os.getcwd()))

# from qtLibPathFacade.qtLibPathFacade import QtLibPathFacade
# main:
#	QtLibPathFacade.addBundledPluginsPath()
