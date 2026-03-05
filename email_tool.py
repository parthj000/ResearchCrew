from langchain_core.tools import tool
from pydantic import BaseModel, Field


class Email(BaseModel):
    subject: str = Field(description="subject for the email")
    body: str = Field(description="main body for the email")
    to: str = Field(description="mail of receiver")
    salutation: str | None = Field(
        description="some intresting salutation to make the email interesting"
    )


@tool(args_schema=Email)
def send_email(subject: str, body: str, to: str, salutation: str) -> str:
    """
    Always use this tool for sending emails
    """
    return "Email has been sent"
