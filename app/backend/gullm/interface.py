# title: interface.py
# Author: Sayan Bandyopadhyay
# Date: 2024-05-05 17:32:48
# Description: This is the interface for the Gullm model. It sends requests to the Gullm server and returns the response.

from enum import Enum
import random
import requests
import json


class Options:
    num_keep: int
    seed: int
    num_predict: int
    top_k: int
    top_p: float
    tfs_z: float
    typical_p: float
    repeat_last_n: int
    temperature: float
    repeat_penalty: float
    presence_penalty: float
    frequency_penalty: float
    mirostat: int
    mirostat_tau: float
    mirostat_eta: float
    penalize_newline: bool
    stop: list[str]
    numa: bool
    num_ctx: int
    num_batch: int
    num_gqa: int
    num_gpu: int
    main_gpu: int
    low_vram: bool
    f16_kv: bool
    vocab_only: bool
    use_mmap: bool
    use_mlock: bool
    rope_frequency_base: float
    rope_frequency_scale: float
    num_thread: int


class GullmInterface:
    def __init__(self, url, model="gullm", stream: bool = False):
        self.url = url
        self.model: str = model
        self.stream: bool = stream
        self.context: list[int] = [
            i for i in range(random.randint(0, 20))
        ]  # Random context for now
        self.options: dict[str, str] = {
            "temperature": 1,
            "penalize_newline": False,
        }  # TODO: Replace with actual options

    def query(self, text: str) -> tuple[str, int]:
        query_url = self.url + "/api/generate"
        response = requests.post(
            query_url,
            json={
                "model": self.model,
                "prompt": text,
                "stream": self.stream,
                "context": self.context,
                "options": self.options,
            },
            stream=True,
        )
        return_message = ""

        # TODO: Stream support is buggy, so use the normal response for now
        if self.stream:
            for chunk in response.iter_content(chunk_size=128):
                if chunk:
                    message = json.loads(chunk.decode("utf-8"))
                    print(message["response"])
                    return_message += message["response"]
            return return_message, response.status_code
        else:
            return response.json()["response"], response.status_code


if __name__ == "__main__":
    gullm = GullmInterface(
        "http://localhost:11434", "gullm", stream=False
    )  # Change the URL to the Gullm server on productions
    message, status = gullm.query("Hi, how are you?")
    print(f"AI: {message}", status)
