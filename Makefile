
install-linux:
	sudo mv dist/linux64/fontmake-mp /usr/local/bin/fontmake-mp

install-macos:
	sudo mv dist/macos64/fontmake-mp /usr/local/bin/fontmake-mp

# Must be executed on Linux 64bit arch system
linux-build:
	rm *.pyc
	pyinstaller -c --onefile --hidden-import=fontmake --clean --distpath="dist/linux64" -n fontmake-mp fmp.py

# Must be executed on macOS 64bit arch system
macos-build:
	rm *.pyc
	pyinstaller -c --onefile --hidden-import=fontmake --clean --distpath="dist/macos64" -n fontmake-mp fmp.py

# cross-platform uninstall for users who installed with make targets above
uninstall:
	rm /usr/local/bin/fontmake-mp

.PHONY: linux-build macos-build install-linux install-macos uninstall