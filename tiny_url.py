"""
Implement a TinyURL service that will take a long URL and return a tiny URL.
Also, implement functions to get, update, and delete the tiny URL.

Example:
long_url = "https://www.google.com"
tiny_url = create_url(long_url)
print(tiny_url)  # Output: "https://tinyurl.com/abc123"

long_url = get_url(tiny_url)
print(long_url)  # Output: "https://www.google.com"

update_url("https://www.google.com", "https://www.facebook.com")
delete_url("https://www.facebook.com")

DB: mysql
Table: tiny_url
Columns: id, long_url, tiny_url, created_at, updated_at
"""

class TinyURL:
    def create_url(self,long_url):
        """
        This function will take a long URL and return a tiny URL.
        :param long_url: str
        :return: str

        Logic:
        1. Generate a random string of 6 characters.
        3. Store the long URL and random string in DB.
        4. Return the random string.

        Note:
        1. If long_url is already present in the DB, return the existing tiny URL.

        Example:
        long_url = "https://www.google.com"
        tiny_url = create_url(long_url)
        print(tiny_url)  # Output: "https://tinyurl.com/abc123"
        """

        return tiny_url

    def get_url(self, tiny_url):
        """
        This function will take a tiny URL and return the long URL.
        :param tiny_url: str
        :return: str

        Logic:
        1. Retrieve the long URL from DB using the tiny URL.
        2. Return the long URL.

        Example:
        tiny_url = "https://tinyurl.com/abc123"
        long_url = get_url(tiny_url)
        print(long_url)  # Output: "https://www.google.com"
        """

        return tiny_url

    def delete_url(self, long_url):
        """
        This function will delete the tiny URL from the DB.
        :param long_url: str
        :return: Boolean

        Logic:
        1. Delete the tiny URL from DB.
        2. Return True if the URL is deleted successfully.
        3. Return False if the URL is not found in the DB.

        Example:
        long_url = "https://www.google.com"
        delete_url(long_url)
        """

        return True

    def update_url(self, old_long_url, new_long_url):
        """
        This function will update the tiny URL with a new long URL.
        :param old_long_url: str
        :param new_long_url: str
        :return: Boolean

        Logic:
        1. Update the tiny URL with the new long URL in DB.
        2. Return True if the URL is updated successfully.
        3. Return False if the URL is not found in the DB.

        Example:
        old_long_url = "https://www.google.com"
        new_long_url = "https://www.facebook.com"
        tiny_url = update_url(old_long_url, new_long_url)
        """

        return True


obj = TinyURL()
url = obj.create_url("https://www.google.com")
print(url) # Output: "https://tinyurl.com/abc123" -- sample output
url = obj.get_url("https://tinyurl.com/abc123")
print(url) # Output: "https://www.google.com" -- sample output
url = obj.update_url("https://www.google.com", "https://www.facebook.com")
print(url)  # Output: True -- sample output
url = obj.delete_url("https://www.facebook.com")
print(url) # Output: True -- sample output