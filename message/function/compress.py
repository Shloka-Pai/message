import zlib

def compress_message(msg: str) -> bytes:
    return zlib.compress(msg.encode())

def decompress_message(data: bytes) -> str:
    return zlib.decompress(data).decode()
