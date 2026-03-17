from io import BytesIO
import uuid
import qrcode
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db
from app.schemas.user import UserCreate, UserRead
from app.service.user_service import UserService

router = APIRouter()

@router.post("/")
async def create_user(
        user_in: UserCreate, 
        db: AsyncSession = Depends(get_db)
    ) -> UserRead:
    
    service = UserService(db)
    return await service.create_user(user_in)

@router.post("/create_qr_code")
async def create_qr_code(
        event_id: uuid.UUID, 
        db: AsyncSession = Depends(get_db)
    ) -> StreamingResponse:
    
    # todo servise tasi 
    service = UserService(db)
    user = service.get_by_id(user_id)
    
    qr = qrcode.make(user)
    buffer = BytesIO(qr, format="PNG")
    buffer.seek(0)
    
    return StreamingResponse(buffer, media_type="image/png")