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
    "days": {"in": "query", "description": "The number of days back to search for events.", "required": False},
    "category": {
        "in": "query",
        "description": "The type of earth event. Categories: drought, wildfires, waterColor, volcanoes,\
            temperatureExtremes, snow, severeStorms, seaAndLakeIce, manmade, landslides, floods, earthquakes, dustAndHaze",
        "required": False
    }
}

futures_params = {
    "ticker_symbol": {"in": "query", "description": "The ticker of the financial instrument to retrieve data from. (Example: AAPL)", "required": False},
    "start_date": {"in": "query", "description": "The date to start the historical query from. (format: YYYY-MM-DD) (Default: 2 days ago)", "required": False},
    "end_date": {"in": "query", "description": "The date to end the historical query from. (format: YYYY-MM-DD) (Default: today)", "required": False}
}
