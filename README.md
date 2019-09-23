# JSON2YAML

A dead simple tool in Python to convert JSON files into YAML.

## Usage

```Shell
$ python3 json2yaml.py [-r] [-s] [-d] PATH
```

where `PATH` is a path string to a JSON file or directory (containing JSON files).

### Optional arguments:

    -r, --recursive  Look for files in subdirectories.
    -s, --sort       Sort the key-value pairs during conversion.
    -d, --delete     Delete file(s) after conversion.

The program uses PyYAML with LibYAML bindings. In order to use the script, you have to install PyYAML and its LibYAML bindings.

On Linux:

```Bash
wget 'http://pyyaml.org/download/libyaml/yaml-0.2.2.tar.gz'
tar -xf yaml-0.2.2.tar.gz
cd yaml-0.2.2/
./configure
make
sudo make install
cd ..
wget 'https://pyyaml.org/download/pyyaml/PyYAML-5.1.2.tar.gz'
tar -xf PyYAML-5.1.2.tar.gz
cd PyYAML-5.1.2/
sudo python3 setup.py --with-libyaml install
cd ..
```

More information and documentation: https://pyyaml.org/
