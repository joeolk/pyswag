payload_validation_failure = {
    "type": "object",
    "properties": {
        "message": {"type": "string"},
        "errors": {
            "type": "object",
            "properties": {
                "error": {
                    "type": "string"
                }
            }
        }
    }
}

internal_server_error = {
    "type": "object",
    "properties": {
        "message": {
            "type": "string"
        }
    }
}

success_resp = {
    "type": "object",
    "properties": {
        "status": {
            "type": "integer"
        },
        "message": {
            "type": "string"
        }
    }
}

earth_event_params = {
    "status": {"in": "query", "description": "'all', 'open', or 'closed'", "required": False},
    "days": {"in": "query", "description": "The number of days back to search for events.", "required": False}
}
