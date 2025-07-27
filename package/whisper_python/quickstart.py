import asyncio
import os
import sys

whisper_python_package_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../package/whisper_python/lib'))
sys.path.append(whisper_python_package_path)

from whisper_python.lib.whisper_python import *


async def main():


    print("start")

    whisperPythonZerounIntezarAgler = WhisperPythonZerounIntezarAgler()
    
    whisperPythonZerounIntezarAgler.ensureInitialized(libraryPath="path_to_library/libname.so")

    def on_callback(update:dict):
        print(update)
    whisperPythonZerounIntezarAgler.on(event_name="update", on_callback=on_callback)

    # debug
    # whisperPythonZerounIntezarAgler.emit(event_name="update", value={
    #     "@type": "ok",
    # });

    await whisperPythonZerounIntezarAgler.initialized();
    whisperPythonZerounIntezarAgler.invokeSync(parameters={
        "@ttyp"
    });
    result = whisperPythonZerounIntezarAgler.invoke(parameters={
        "@type": "getMe",
    });
    print(result) 

    print("done")


asyncio.run(main())


