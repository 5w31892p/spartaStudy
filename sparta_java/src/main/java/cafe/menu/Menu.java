package cafe.menu;

import java.util.ArrayList;
import java.util.List;

public class Menu {
    private final List<MenuItem> menuItemsList = new ArrayList<>();

    public Menu() {
        this.menuItemsList.add(new MenuItem("아메리카노", 1000));
        this.menuItemsList.add(new MenuItem("라떼", 2000));
        this.menuItemsList.add(new MenuItem("오렌지쥬스", 3000));
        this.menuItemsList.add(new MenuItem("밀크셰이크", 4000));
        this.menuItemsList.add(new MenuItem("프라푸치노", 6000));
        this.menuItemsList.add(new MenuItem("버블티", 8000));
    }
    public MenuItem getMenuItem(String menuName) {
        for (MenuItem menuItem : this.menuItemsList) {
            if (menuItem.getName().equals(menuName)) {
                return menuItem;
            }
        }
        throw new IllegalArgumentException("존재하지 않는 메뉴입니다.");
    }
    public List<MenuItem> getMenuItemsList() {
        return menuItemsList;
    }
}
