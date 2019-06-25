# kusu | Kieran's Useful Script Utilities

install using:
`pip install kusu`

or download the source with:
`git clone https://github.com/Descent098/kusu`

There is inline documentation and 

# Official Documentation
There is some readthedocs documentation with examples available at:

__*comming soon*__

## Logging
The configuration for logging in project files can be found below. 

### Default Configuration
 
#### File output
By default logs go to ```LOG_FOLDER/LOG_FILE_FORMAT``` specified in the main runfile, or in the logger.py itself. Currently this is configured to save logs to /utilities/logs/<date>-main.log
 
#### Formatting
The default log format is ```<Current time> | <severity> | <module name> | : <log message> ```. This can be modified by overriding the LOG_FORMAT variable in logger.py.

### Setup Logging

#### In main module use
```python
from utilities.logger import setup_primary_logger
PRIMARY_LOGGER = setup_primary_logger("Main")
PRIMARY_LOGGER.debug("message from main")
```
#### In submodules use
```python
import logging
logger = logging.getLogger('root')
logger.debug('submodule message')
```