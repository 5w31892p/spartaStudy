package cafe.menu.repository;

import cafe.menu.Menu;
import cafe.menu.MenuItem;

public class SpringMenuRepository implements MenuRepository{
    // Mysql에 넣었다 뻈다.
    @Override
    public void saveMenu(Menu menu) {

    }

    @Override
    public MenuItem getMenuItem(int id, String menuName) {
        return null;
    }

    @Override
    public Menu getMenu(int id) {
        return null;
    }
}
