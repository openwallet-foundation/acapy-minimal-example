# Template

A template for creating examples in AME. Simply copy this folder into `examples`, rename, and modify `example.py` and the docker-compose as necessary. There are several examples there that you can use for inspiration. This example simply connects two ACA-Py instances.

To run:
```
docker-compose build
docker-compose run --rm example
# Clean up
docker-compose down -v
```