## Changelog

### v1.0.0

- added `--ttf` and `--otf` options to support definition of desired build file type
- added support for parallel *.ttf and *.otf builds when they are requested in the same command. This means that parallel builds are now performed for every VARIANT x FILE TYPE combination in the command up to the number of processing units available on your machine.  Prior to this version, support was provided for parallel builds across font variants only
- added help options and in-application help documentation
- added usage option and in-application usage documentation
- added version options and in-application version report

### v0.9.1

- updated user message strings during script execution
- fixed incorrect stderr string test that led to test failures
- added version string to the header of the fmp.py Python script

### v0.9.0

- initial release
