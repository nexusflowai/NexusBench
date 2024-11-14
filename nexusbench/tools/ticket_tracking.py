from typing import List


def search_tickets(statuses: List[str]):
    """
    This function searches for software engineering tickets by their status.
    The query by the engineer can mention multiple statuses or none of the statuses.

    Available statuses:
    - 'PENDING': The ticket is newly created and needs action from the engineer.
    - 'IN_PROGRESS': The ticket is actively being worked on by the engineer.
    - 'REVIEW_REQUESTED': The engineer has requested review of the ticket from other engineers.
    - 'WAITING_FOR_USER': The engineer has requested more information about the ticket from the user and the user has not responded. The engineer is now blocked by user.
    - 'USER_RESPONSE_RECEIVED': A response has been received from the user (The engineer is unblocked and needs to review responses).
    - 'RESOLVED': The ticket is successfully closed (investigation completed), not active anymore, or does not need action from anyone anymore.
    - 'CANCELLED': The ticket is unsuccessfully closed.
    """


search_tickets_json = {
    "name": "search_tickets",
    "description": "This function searches for software engineering tickets by their status. The query by the engineer can mention multiple statuses or none of the statuses.",
    "parameters": {
        "type": "object",
        "properties": {
            "statuses": {
                "type": "array",
                "items": {
                    "type": "string",
                    "enum": [
                        "PENDING",
                        "IN_PROGRESS",
                        "REVIEW_REQUESTED",
                        "WAITING_FOR_USER",
                        "USER_RESPONSE_RECEIVED",
                        "RESOLVED",
                        "CANCELLED",
                    ],
                },
                "description": """This function searches for software engineering tickets by their status. \n\
The query by the engineer can mention multiple statuses or none of the statuses.\n\
\n\
Available statuses:\n\
- 'PENDING': The ticket is newly created and needs action from the engineer.\n\
- 'IN_PROGRESS': The ticket is actively being worked on by the engineer.\n\
- 'REVIEW_REQUESTED': The engineer has requested review of the ticket from other engineers.\n\
- 'WAITING_FOR_USER': The engineer has requested more information about the ticket from the user and the user has not responded. The engineer is now blocked by user.\n\
- 'USER_RESPONSE_RECEIVED': A response has been received from the user (The engineer is unblocked and needs to review responses).\n\
- 'RESOLVED': The ticket is successfully closed (investigation completed), not active anymore, or does not need action from anyone anymore.\n\
- 'CANCELLED': The ticket is unsuccessfully closed.""",
            }
        },
        "required": ["statuses"],
    },
}
