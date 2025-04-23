from db import db
class ItemTags(db.Model):
    __tablename__ = "item_tags"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"), nullable=False)

    #item = db.relationship("ItemModel", back_populates="tags")
    #tag = db.relationship("TagModel", back_populates="items")
    #__table_args__ = (db.UniqueConstraint("item_id", "tag_id", name="unique_item_tag"),)