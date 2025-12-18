"""
Simple HTTP server module.
This module provides a basic HTTP server for testing purposes.
"""

import http.server
import socketserver

PORT = 8000


class TestMe():
    """Test class with utility methods."""
    
    def take_five(self):
        """
        Return the number five.
        
        Returns:
            int: The number 5
        """
        return 5  # Было 4, стало 5
    
    def port(self):
        """
        Get the server port number.
        
        Returns:
            int: The port number (8000)
        """
        return PORT


if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port", PORT)
        http.serve_forever()