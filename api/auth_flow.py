from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


# Define your app's authorization scopes.
# When modifying these scopes, delete the file token.json, if it exists.
SCOPES = ["https://www.googleapis.com/auth/chat.spaces.create"]

def main():
  '''
  Authenticates with Chat API via user credentials,
  then creates a Chat space.
  '''

  client_secrets = 'client_secret_285651774856-v45nurf04diin6bsgmliq08id6jvsiap.apps.googleusercontent.com.json'

  flow = InstalledAppFlow.from_client_secrets_file(
                    client_secrets, SCOPES)
  creds = flow.run_local_server()

  # Build a service endpoint for Chat API.
  service = build('chat', 'v1', credentials=creds)

  # Use the service endpoint to call Chat API.
  result = service.spaces().create(

    # Details about the space to create.
    body = {

      # To create a named space, set spaceType to SPACE.
      'spaceType': 'SPACE',

      # The user-visible name of the space.
      'displayName': 'API-made'

    }

  ).execute()

  # Prints details about the created space.
  print(result)

if __name__ == '__main__':
  main()