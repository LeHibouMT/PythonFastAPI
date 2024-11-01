from fastapi import APIRouter, Depends, HTTPException
from app.database import AsyncSessionLocal
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Item, ItemModel

router = APIRouter()

async def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/items/{item_id}")
async def get_item(item_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Item).where(Item.id == item_id))
    item = result.scalars().first()
    
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return item

@router.post("/items/", status_code=201)
async def create_item(item: ItemModel, db: AsyncSession = Depends(get_db)):
    new_item = Item(name=item.name, description=item.description)
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)
    return new_item

@router.put("/items/{item_id}")
async def update_item(item_id: int, item: ItemModel, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Item).where(Item.id == item_id))
    existing_item = result.scalars().first()

    if existing_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.name is not None:
        existing_item.name = item.name
    if item.description is not None:
        existing_item.description = item.description

    await db.commit()
    await db.refresh(existing_item)
    return existing_item
    
@router.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Item).where(Item.id == item_id))
    existing_item = result.scalars().first()

    if existing_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    await db.delete(existing_item)
    await db.commit()
    return {"detail": f"Item {existing_item.id} deleted successfully"}

