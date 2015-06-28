from distutils.core import setup
import py2exe, sys, os, shutil

sys.argv.append('py2exe')

if os.path.exists('dist'):
	shutil.rmtree('dist')

install = dict(script="BasementBuilder.py",
		dest_base="Basement Builder",
		icon_resources=[(0, "resources/UI/BasementBuilder.ico")])

setup(
	name="Basement Builder",
	version="1.0",
	author="Zatherz, Tempus, Jean-Alphonse",
	author_email="Zatherz@linux.pl, Tempus@chronometry.ca",
	windows = [{'script': "BasementBuilder.py"}],
	options = {'py2exe': {
		'bundle_files': 1, 
		'compressed': False, 
		"includes":["sip", "xml.etree"],
		'optimize': 2,
		'bundle_files': 3,
	}}
)


os.mkdir('dist/platforms')
shutil.copytree('resources', 'dist/resources')
shutil.copy('C:\\Python34/Lib/site-packages/PyQt5/plugins/platforms/qwindows.dll', 'dist/platforms')
shutil.copy('C:\\Python34/Lib/site-packages/PyQt5/libEGL.dll', 'dist')
