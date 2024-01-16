# Scanling
![](search.png)
## Description
<p>Scanling is a python commandline tool, which i wrote to port scan a single ip address or a range of ip addresses.</p>

## Installation
```bash
pip3 install requirements.txt
```

## Usage
```bash
# default port scan for single ip
python3 scanling.py -ip 10.1.10.118

# default port scan for ip range
python3 scanling.py -iprange 10.1.10.118-10.1.10.120
```

## Parameters
| **Parameter** | **Description**                                                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| -ip         | Runs a port scan for a single ip address.                                                                          |
| -iprange            | Runs a port scan for a range of ip addresses. |
