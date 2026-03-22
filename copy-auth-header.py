from burp import IBurpExtender, IContextMenuFactory
from javax.swing import JMenuItem
from java.util import ArrayList
from java.awt import Toolkit
from java.awt.datatransfer import StringSelection


class BurpExtender(IBurpExtender, IContextMenuFactory):

    def registerExtenderCallbacks(self, callbacks):
        self.callbacks = callbacks
        self.helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Copy Auth Headers")
        callbacks.registerContextMenuFactory(self)

    def createMenuItems(self, invocation):

        menu = ArrayList()
        menuItem = JMenuItem(
            "Copy Auth Headers",
            actionPerformed=lambda x: self.copyHeaders(invocation)
        )

        menu.add(menuItem)
        return menu

    def copyHeaders(self, invocation):

        messages = invocation.getSelectedMessages()

        if not messages:
            return

        request = messages[0].getRequest()
        analyzed = self.helpers.analyzeRequest(request)

        headers = analyzed.getHeaders()

        found_headers = []

        for header in headers:
            header_lower = header.lower()

            if header_lower.startswith("cookie:"):
                found_headers.append(header)
            if header_lower.startswith("x-api-key:"):
                found_headers.append(header)
            if header_lower.startswith("x-auth-key:"):
                found_headers.append(header)
            if header_lower.startswith("authorization:"):
                found_headers.append(header)

        if not found_headers:
            return

        result = "\n".join(found_headers)

        clipboard = Toolkit.getDefaultToolkit().getSystemClipboard()
        clipboard.setContents(StringSelection(result), None)