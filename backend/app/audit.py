import uuid

from sqlmodel import Session

from app.models import AuditLog


def log_action(
    session: Session,
    org_id: uuid.UUID,
    action: str,
    target_id: uuid.UUID | None = None,
    details: str | None = None,
):
    eintrag = AuditLog(
        org_id=org_id,
        action=action,
        target_id=target_id,
        details=details,
    )
    session.add(eintrag)
