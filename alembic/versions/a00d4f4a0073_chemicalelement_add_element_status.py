"""ChemicalElement add element_status

Revision ID: a00d4f4a0073
Revises: de6ceeecc6fe
Create Date: 2024-04-11 00:21:17.751347

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a00d4f4a0073'
down_revision: Union[str, None] = 'de6ceeecc6fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'chemical_element',
        sa.Column('element_status', sa.String(10), nullable=False)
    )


def downgrade() -> None:
    op.drop_column('chemical_element', 'element_status')
