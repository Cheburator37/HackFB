import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))