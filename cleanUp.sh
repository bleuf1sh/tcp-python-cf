#!/bin/bash
echo 'Attempting "rm -rf ./src/__pycache__"'
rm -rf './src/__pycache__' || true

echo 'Attempting "rm -rf ./live-mitm-config"'
rm -rf './live-mitm-config' || true