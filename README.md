# python3.js
Call python code from node.js.

## Usage

```javascript
var python = require('python.js');
var os = python.import('os');

var path = require('path');

assert(os.path.basename(os.getcwd()) == path.basename(process.cwd()));
```

## Feature

```python
def test():
	try:
		## do samething
	except Exception as e:
		raise e
	return 'done'
```

```javascript
PYMODULE.test.async = true;
PYMODULE.test(function (result, error) {
	if (!error)
		console.log(result);
});
```

## Build

```bash
$apt-get install python3-dev
$git clone https://github.com/xhsiung/python3.js
$cd python3.js 
$node-gyp configure build 
```

## Test

```bash
node test/jstest.js
```


## Thanks

* [Jean-Sébastien Tremblay](https://github.com/JeanSebTr/node-python)
* [Chris Dickinson](https://github.com/chrisdickinson/node-python)
* [monkeycz](https://github.com/monkeycz/python.js.git)
