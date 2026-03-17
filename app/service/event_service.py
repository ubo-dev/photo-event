
import uuid
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.event import Event
from app.repository.event_repository import EventRepository

class EventService:
    
    def __init__(self, db: AsyncSession):
        self.repository = EventRepository(db)
    
    async def get_by_id(self, id: uuid.UUID) -> Event:
        existing_event = await self.repository.get_by_id(id)
        if existing_event is None:
            raise HTTPException(status_code=404, detail="No event found with given id!")
        
        return existing_event
        
            