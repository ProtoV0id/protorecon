#Creates the session state.
class SessionState:
    def __init__(self):
        #workspaces *notice the s* is the session workspaces created or available
        self.workspaces=["default"]

        #default workspace is default. This stores active workspace
        self.workspace="default"

        #module name if selected
        self.loaded_module=None

        # Stores every target added during this session. No default target
        self.targets = []

        # Stores the currently selected target.
        # None means no target has been selected yet.
        self.target = None

        #main loop control. Changes to False when the user quits/exits
        self.running=True
