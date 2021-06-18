ERROR_ON_SEND_LAYOUT = {
    "type": "object",
    "properties": {
        "non_field_errors": {
            "type": "array",
            "items": {
                "type": "string",
            },
            "description": "Contains errors on bussiness logic (Ex. repeated data)"
        },
        "field_name": {
            "type": "array",
            "items": {
                "type": "string",
            },
            "description": "Contains errors on field (Ex. invalid type) - OBS: each field with error generate a line"
        },
    }
}
