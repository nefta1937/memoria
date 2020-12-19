import time
from orchestrator import Orchestrator

orchestrator = Orchestrator()
orchestrator.run()
print('sleeping orchestrator for 30 seconds')
time.sleep(30)
orchestrator.stop()
print('process finished')