# ACA-Py ME Examples

This directory contains a number of examples that use the ACA-Py Minimal Example. These examples have proven useful for testing and demonstrating the capabilities of the ACA-Py Minimal Example -- useful enough to be shared with others. Use these examples as a starting point for your own experiments and integrations.
Each example is self-contained in its own directory. Each contains a `docker-compose.yml` file that defines the services used in the example, and an `example.py` script that implements the logic of the example. To run an example, `cd` into its directory and run:

```sh
docker-compose up -d
python example.py
``` 

When you are done, you can stop and remove all running containers with:

```sh
docker-compose down -v
```

If you create an example that you think would be useful to others, please consider contributing it to this repository! Follow the guidance in the [Template Example](./template/README.md) to as a guide for creating a PR to add your example to this repository.
