from flask import Request
def create_server(request : Request ):
    # Draw from server templates
    

    # Pre-fill server template

    # Run server template in pipeline

    # verify server creation

    # store server config in DB and relate to user


    return f'Server created successfully for {request.form["name"]}', 201