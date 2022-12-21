package cafe.menu;

public interface MenuService {
    void  createMenu();
    MenuItem getMenuItem(int id, String menuName);
    Menu getMenu(int id);
}
