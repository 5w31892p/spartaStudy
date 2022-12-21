package cafe.menu;

import cafe.menu.repository.JavaMenuRepository;
import cafe.menu.repository.MenuRepository;

public class JavaMenuService implements MenuService{
    private final MenuRepository menuRepository = new JavaMenuRepository();
    @Override
    public void createMenu() {
        // 코드가 들어갈 수도 있음
        menuRepository.saveMenu(new Menu());
    }

    @Override
    public MenuItem getMenuItem(int id, String menuName) {
        return menuRepository.getMenuItem(id, menuName);
    }

    @Override
    public Menu getMenu(int id) {
        return menuRepository.getMenu(id);
    }
}
