import asyncio
import os
import sys

whisper_python_package_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../package/whisper_python/lib'))
sys.path.append(whisper_python_package_path)

from whisper_python import *

async def main():


    print("start")

    whisperPythonZerounIntezarAgler = WhisperPythonZerounIntezarAgler()
    
    whisperPythonZerounIntezarAgler.ensureInitialized(libraryPath="fork/dependencies/lib/libwhisper_gpl.so")
 
    result =await whisperPythonZerounIntezarAgler.loadModelFromFilePath(whisperModelFilePath="../../../big-data/whisper/ggml-base.en.bin")
    print(result)
    
    translate=await whisperPythonZerounIntezarAgler.transcribeFromFilePath(file_path="../../../fork/whisper.cpp/samples/jfk.mp3")
    print(translate)
    # debug
    # whisperPythonZerounIntezarAgler.emit(event_name="update", value={
    #     "@type": "ok",
    # });
 


asyncio.run(main())


