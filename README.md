# python-blockchain

**Activate the virtual environment**

```
source blockchain-env/bin/activate
```

**Install all packages**
```
pip3 install -r requirements.txt
```

**Run the tests**
```
python3 -m pytest backend/tests
```

**Run the application and API**

```
python3 -m backend.app
```

**Run a peer instance**

Make sure to activate the virtual environment.

```
export PEER=TRUE && python3 -m backend.app
```
