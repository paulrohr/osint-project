import uuid
from datetime import datetime, timezone

from sqlalchemy import DateTime, UniqueConstraint
from sqlmodel import Field, SQLModel


def jetzt() -> datetime:
    return datetime.now(timezone.utc)


class Organization(SQLModel, table=True):
    __tablename__ = "organizations"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    created_at: datetime = Field(
        default_factory=jetzt, sa_type=DateTime(timezone=True))


class Case(SQLModel, table=True):
    __tablename__ = "cases"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    org_id: uuid.UUID = Field(foreign_key="organizations.id", index=True)
    title: str
    purpose: str
    created_at: datetime = Field(
        default_factory=jetzt, sa_type=DateTime(timezone=True))


class Entity(SQLModel, table=True):
    __tablename__ = "entities"
    __table_args__ = (UniqueConstraint("case_id", "type", "value"),)

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    org_id: uuid.UUID = Field(foreign_key="organizations.id", index=True)
    case_id: uuid.UUID = Field(foreign_key="cases.id", index=True)
    type: str
    value: str
    created_at: datetime = Field(
        default_factory=jetzt, sa_type=DateTime(timezone=True))


class Finding(SQLModel, table=True):
    __tablename__ = "findings"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    org_id: uuid.UUID = Field(foreign_key="organizations.id", index=True)
    entity_id: uuid.UUID = Field(foreign_key="entities.id", index=True)
    key: str
    value: str
    source: str
    created_at: datetime = Field(
        default_factory=jetzt, sa_type=DateTime(timezone=True))


class EntityLink(SQLModel, table=True):
    __tablename__ = "entity_links"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    org_id: uuid.UUID = Field(foreign_key="organizations.id", index=True)
    case_id: uuid.UUID = Field(foreign_key="cases.id", index=True)
    from_entity_id: uuid.UUID = Field(foreign_key="entities.id")
    to_entity_id: uuid.UUID = Field(foreign_key="entities.id")
    relation: str
    source: str
    created_at: datetime = Field(
        default_factory=jetzt, sa_type=DateTime(timezone=True))


class AuditLog(SQLModel, table=True):
    __tablename__ = "audit_log"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    org_id: uuid.UUID = Field(foreign_key="organizations.id", index=True)
    action: str
    details: str | None = None
    target_id: uuid.UUID | None = None
    created_at: datetime = Field(
        default_factory=jetzt, sa_type=DateTime(timezone=True))
