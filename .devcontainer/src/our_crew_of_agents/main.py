from dotenv import load_dotenv

load_dotenv()
from crew import OurCrewOfAgents

import os
import agentops

agentops.init(os.getenv("AGENTOPS_API_KEY"))

print("Calling our crew of agents...")
OurCrewOfAgents().crew().kickoff()
