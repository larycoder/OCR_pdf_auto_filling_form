import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;
import java.io.*; 

class test{
  private static int i = 0;

  private static ArrayList readFile(String filename) throws Exception{
    ArrayList fields = new ArrayList();
    File file = new File(filename);
    BufferedReader br = new BufferedReader(new FileReader(file)); 
  
    String st; 
    while ((st = br.readLine()) != null){ 
       fields.add(st);
    } 
    return fields;
  }
  public static void main(String[] args) throws Exception{
    ArrayList fields = readFile(args[0]);
    ArrayList values = new ArrayList();

    JFrame mainFrame = new JFrame("Input");
    mainFrame.setLayout(new BorderLayout(10, 20));
    mainFrame.setSize(400, 400);
    mainFrame.addWindowListener(new WindowAdapter() {
         public void windowClosing(WindowEvent windowEvent){
            System.exit(0);
         }        
    });

    JLabel headerLabel = new JLabel(fields.get(i).toString(), JLabel.CENTER);
    JButton button = new JButton("submit");
    JTextField textField = new JTextField();
    

    button.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        headerLabel.setText(fields.get(i).toString());
        values.add(textField.getText());
        textField.setText("");
        i = i + 1;
        if (i >= fields.size()){
          try{
            FileWriter writer = new FileWriter("user_value.txt"); 
            for(int j = 0; j < values.size(); j++) {
              writer.write(values.get(j).toString() + System.lineSeparator());
            }
            writer.close();
          } catch(Exception E) {}
          System.exit(1);
        }
      }
    });

    

    mainFrame.add(headerLabel, BorderLayout.NORTH);
    mainFrame.add(textField, BorderLayout.CENTER);
    mainFrame.add(button, BorderLayout.SOUTH);
    
    mainFrame.setVisible(true);
  }
}