from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config
from sqlalchemy import pool

from src.config import DataBaseConfig
from src.crm.infrastructure.database.database import Base
from src.crm.infrastructure.models.branches import CompanyBranch
from src.crm.infrastructure.models.categories import Category
from src.crm.infrastructure.models.companies import Company
from src.crm.infrastructure.models.deals import Deal
from src.crm.infrastructure.models.employees import Employee
from src.crm.infrastructure.models.leads import Lead
from src.crm.infrastructure.models.product_category import ProductsCategory
from src.crm.infrastructure.models.products import Product
from src.crm.infrastructure.models.users import User
from src.crm.infrastructure.models.warehouse import Warehouse
from src.crm.infrastructure.models.warehouse_products import WarehouseProducts
from src.crm.infrastructure.models.warehouse_transfers import WarehouseTransfer

__tables__ = [
    User,
    Company,
    CompanyBranch,
    Product,
    Employee,
    Warehouse,
    Category,
    ProductsCategory,
    WarehouseProducts,
    WarehouseTransfer,
    Deal,
    Lead,
]

config = context.config
config.set_main_option('sqlalchemy.url', DataBaseConfig().get_db_url)
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
