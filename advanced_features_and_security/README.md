# Permissions and Groups Setup

## Custom Permissions
Defined in `bookshelf/models.py` under the `Book` model:
- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

## Groups
Created via Django admin:
- **Viewers**: Assigned `can_view`
- **Editors**: Assigned `can_create`, `can_edit`
- **Admins**: Assigned all permissions

## Views
Protected using `@permission_required` decorators in `bookshelf/views.py`.

## Testing
Test users were assigned to groups and verified for access control.
