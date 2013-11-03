all: protoc protolite

protoc: force
	protoc --python_out=. messages.proto

protolite: force
	PYTHONPATH=../ python -c 'from protolite.cli.protolitec import main; main()' messages.proto .

force: ;
