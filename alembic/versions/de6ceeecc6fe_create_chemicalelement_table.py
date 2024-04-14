"""create ChemicalElement table

Revision ID: de6ceeecc6fe
Revises: 
Create Date: 2024-04-10 23:45:51.264841

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de6ceeecc6fe'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'chemical_element',
        sa.Column('atomic_num', sa.Integer, primary_key=True),
        sa.Column('element_type', sa.String(10), nullable=True),
        sa.Column('element_symbol', sa.String(10), nullable=False),
        sa.Column('name', sa.String(10), nullable=False),
        sa.Column('atomic_mass', sa.REAL, nullable=False),
        sa.Column('electron_shells', sa.Text, nullable=False),
        sa.Column('fusing_point', sa.REAL, nullable=True),
        sa.Column('boiling_point', sa.REAL, nullable=True),
        sa.Column('energy_level', sa.Integer, nullable=False),
        sa.Column('electronegativity', sa.REAL, nullable=True),
        sa.Column('electronic_affinity', sa.REAL, nullable=True),
        sa.Column('encyclopedia_entry', sa.Text, nullable=True),
        sa.Column('year_of_discovery', sa.String(10), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('chemical_element')
