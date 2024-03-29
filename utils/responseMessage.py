response_data = {
    "OK001": "User Created Successfully",
    "OK002": "User Updated Successfully",
    "OK003": "User has been Deleted",
    "OK004": "Password has been Changed",
    "OK005": "Logged in successfully",
    "ER999":"Something went wrong",
    "ER901": "Please Authenticate",
    "ER902": "No User Found",
    "ER903": "User Account is Deleted"
}

def response_message(code):
    message = response_data.get(code)
    if message is None:
        raise Exception(f"The code {code} is not matched to any response_data")
    return {"code": code, "message": message}

