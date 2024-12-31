- Move to project with: cd /path-to-project
- Active virtual environment for python: source venv/bin/activate
- If you want to run combine audio with silent, run this command: python3 combine_has_silent.py
=> Result: output-has-silent-{timestamp}.wav
- If you want to run combine audio not has silent, run this command: python3 combine_not_has_silent.py
=> Result: output-has-not-silent-{timestamp}.wav
- If you want to run combine audio with overlay, run this command: python3 comine_with_overlay.py
=> Result: output-with-overlay-{timestamp}.wav
- Deactive virtual environment for python: deactivate

#NOTE: 
- If your project require ffmpeg to run. Please install ffmpeg
- Run commmand: brew install ffmpeg
- Check version: ffmpeg -version
- Uncomment code in this line: AudioSegment.converter = "/usr/local/bin/ffmpeg"
- Change path to ffmpeg
- Done. Project working